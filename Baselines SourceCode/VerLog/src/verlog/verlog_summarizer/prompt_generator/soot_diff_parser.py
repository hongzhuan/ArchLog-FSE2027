import json
from utils import string_util
from prompt_generator.method_hunk_matcher import (
    HunkMatcher,
    ModifiedMethodMatchStrategy, 
    AddedMethodMatchStrategy, 
    DeletedMethodMatchStrategy,
    hunk_matcher_factory
)

from prompt_generator import git_diff_parser
from prompt_generator.augmented_method import AugmentedMethod


def __parse_one_added_or_deleted_method(method_info, method_changed_category, diff_hunks):
    '''
    Parse one changed method
    '''
    method_name = method_info['method_name']
    unformatted_method_line_nums = method_info['line_number']
    method_line_nums = string_util.format_method_line_nums(unformatted_method_line_nums)
    reachable_methods = method_info['reachable_methods']
    # Skip methods without line numbers (0-0)
    if method_line_nums == (0, 0):
        return None
    method_hunk_matcher = HunkMatcher(hunk_matcher_factory(method_changed_category))
    matched_lines = method_hunk_matcher.get_matched_lines(method_name, method_line_nums, diff_hunks)
    augmented_method = AugmentedMethod(method_name, 
                                       method_changed_category, 
                                       method_line_nums, 
                                       reachable_methods, 
                                       matched_lines)
    return augmented_method

def __parse_two_modified_methods(method_info_ref, method_info_tgt, method_changed_category, diff_hunks):
    '''
    Parse two modified methods
    '''
    if method_info_ref is None or method_info_tgt is None:
        return None, None
    method_name = method_info_tgt['method_name']
    unformatted_method_line_nums_ref = method_info_ref['line_number']
    unformatted_method_line_nums_tgt = method_info_tgt['line_number']
    method_line_nums_ref = string_util.format_method_line_nums(unformatted_method_line_nums_ref)
    method_line_nums_tgt = string_util.format_method_line_nums(unformatted_method_line_nums_tgt)
    reachable_methods_ref = method_info_ref['reachable_methods']
    reachable_methods_tgt = method_info_tgt['reachable_methods']
    # Skip methods without line numbers (0-0)
    if method_line_nums_tgt == (0, 0):
        return None
    method_hunk_matcher = HunkMatcher(hunk_matcher_factory(method_changed_category))
    matched_lines = method_hunk_matcher.get_matched_lines(method_name, method_line_nums_tgt, diff_hunks)
    augmented_method_ref = AugmentedMethod(method_name, 'MODIFIED_METHODS_IN_REF_CLASS', method_line_nums_ref, reachable_methods_ref, matched_lines)
    augmented_method_tgt = AugmentedMethod(method_name, 'MODIFIED_METHODS_IN_TGT_CLASS', method_line_nums_tgt, reachable_methods_tgt, matched_lines)
    return augmented_method_ref, augmented_method_tgt

def __same_method_name(method_name_ref, method_name_tgt):
    if method_name_ref == method_name_tgt:
        return True
    return (
        string_util.extract_function_name_from_method_signature(method_name_ref)
        == string_util.extract_function_name_from_method_signature(method_name_tgt)
    )

def __find_matching_tgt_method(ref_method, ref_method_index, tgt_methods, used_tgt_indexes):
    method_name = ref_method['method_name']

    for i, tgt_method in enumerate(tgt_methods):
        if i in used_tgt_indexes:
            continue
        tgt_method_name = tgt_method['method_name']
        if __same_method_name(method_name, tgt_method_name):
            used_tgt_indexes.add(i)
            return tgt_method

    # C/C++ diff generation can intentionally pair renamed or moved functions.
    # In that case the ref/tgt arrays are emitted in pair order, even though the
    # names no longer match.
    if ref_method_index < len(tgt_methods) and ref_method_index not in used_tgt_indexes:
        used_tgt_indexes.add(ref_method_index)
        return tgt_methods[ref_method_index]

    return None

def __get_hunks_from_patch_set(patch_set, file_path):
    '''
    Get hunks from patch set, and the file path contains the class name
    '''
    normalized_file_path = __normalize_patch_path(file_path)
    for file in patch_set:
        patch_paths = {
            __normalize_patch_path(file.path),
            __normalize_patch_path(file.source_file),
            __normalize_patch_path(file.target_file),
        }
        if normalized_file_path in patch_paths:
            return file
    return []

def __normalize_patch_path(file_path):
    if not file_path:
        return ""
    file_path = str(file_path).replace("\\", "/")
    if file_path.startswith("a/") or file_path.startswith("b/"):
        file_path = file_path[2:]
    return file_path

def get_parsed_diff_result(soot_diff_result_file, tag1, tag2, repo_path):
    '''
    Parse the diff result and return a more handly result
    '''
    with open(soot_diff_result_file, encoding='utf-8') as f:
        diff_result = json.load(f)
    diff_patchset = git_diff_parser.get_patchset_from_subshell(tag1, tag2, repo_path)

    # Extract added, modified, and deleted activities
    added_activities = [act for act in diff_result['added_classes']]
    modified_activities = [act for act in diff_result['modified_classes']]
    deleted_activities = [act for act in diff_result['deleted_classes']]


    augmented_methods = []

    for activity in modified_activities:
        diff_hunks = __get_hunks_from_patch_set(diff_patchset, activity['class_name'])
        for method in activity['ADDED_METHOD_IN_MODIFIED_CLASS']:
            augmented_method = __parse_one_added_or_deleted_method(method, 'ADDED_METHOD_IN_MODIFIED_CLASS', diff_hunks)
            if augmented_method:
                augmented_methods.append(augmented_method)

        tgt_methods = activity['MODIFIED_METHOD_IN_TGT_CLASS']
        used_tgt_indexes = set()

        for ref_method_index, ref_method in enumerate(activity['MODIFIED_METHOD_IN_REF_CLASS']):
            tgt_method = __find_matching_tgt_method(
                ref_method,
                ref_method_index,
                tgt_methods,
                used_tgt_indexes,
            )

            augmented_ref_method, augmented_tgt_method = __parse_two_modified_methods(ref_method,
                                                                                      tgt_method,
                                                                                      'MODIFIED_METHOD_IN_MODIFIED_CLASS',
                                                                                      diff_hunks)
            if augmented_ref_method and augmented_tgt_method:
                augmented_methods.append(augmented_ref_method)
                augmented_methods.append(augmented_tgt_method)
            

        for method in activity['DELETED_METHOD_IN_MODIFIED_CLASS']:
            augmented_method = __parse_one_added_or_deleted_method(method, 'DELETED_METHOD_IN_MODIFIED_CLASS', diff_hunks)
            if augmented_method:
                augmented_methods.append(augmented_method)

    for activity in added_activities:
        diff_hunks = __get_hunks_from_patch_set(diff_patchset, activity['class_name'])
        for method in activity['ADDED_METHOD_IN_ADDED_CLASS']:
            augmented_method = __parse_one_added_or_deleted_method(method, 'ADDED_METHOD_IN_ADDED_CLASS', diff_hunks)
            if augmented_method:
                augmented_methods.append(augmented_method)

    for activity in deleted_activities:
        diff_hunks = __get_hunks_from_patch_set(diff_patchset, activity['class_name'])
        for method in activity['DELETED_METHOD_IN_DELETED_CLASS']:
            augmented_method = __parse_one_added_or_deleted_method(method, 'DELETED_METHOD_IN_DELETED_CLASS', diff_hunks)
            if augmented_method:
                augmented_methods.append(augmented_method)

    #filtered_augmented_methods = __filter_augmented_methods(augmented_methods)
    
    return augmented_methods
