package entity;

import java.util.*;

public class JNITypeRegistry {
    //
    private static final Map<String, JNITypeInfo> typeMap = new HashMap<>();

    //
    static {
        loadDefaultTypes();
    }

    //
    private JNITypeRegistry() {}

    private static void loadDefaultTypes() {
        //
        addType(new JNITypeInfo("jboolean", "boolean", "jboolean", false, "8-bit boolean"));
        addType(new JNITypeInfo("jbyte", "byte", "jbyte", false, "8-bit signed integer"));
        addType(new JNITypeInfo("jchar", "char", "jchar", false, "16-bit unsigned Unicode character"));
        addType(new JNITypeInfo("jshort", "short", "jshort", false, "16-bit signed integer"));
        addType(new JNITypeInfo("jint", "int", "jint", false, "32-bit signed integer"));
        addType(new JNITypeInfo("jlong", "long", "jlong", false, "64-bit signed integer"));
        addType(new JNITypeInfo("jfloat", "float", "jfloat", false, "32-bit floating point"));
        addType(new JNITypeInfo("jdouble", "double", "jdouble", false, "64-bit floating point"));
        addType(new JNITypeInfo("jvoid", "void", "void", false, "void type"));

        //
        addType(new JNITypeInfo("jbooleanArray", "boolean[]", "jbooleanArray", true, "Array of boolean"));
        addType(new JNITypeInfo("jbyteArray", "byte[]", "jbyteArray", true, "Array of bytes"));
        addType(new JNITypeInfo("jcharArray", "char[]", "jcharArray", true, "Array of chars"));
        addType(new JNITypeInfo("jshortArray", "short[]", "jshortArray", true, "Array of shorts"));
        addType(new JNITypeInfo("jintArray", "int[]", "jintArray", true, "Array of ints"));
        addType(new JNITypeInfo("jlongArray", "long[]", "jlongArray", true, "Array of longs"));
        addType(new JNITypeInfo("jfloatArray", "float[]", "jfloatArray", true, "Array of floats"));
        addType(new JNITypeInfo("jdoubleArray", "double[]", "jdoubleArray", true, "Array of doubles"));

        //
        addType(new JNITypeInfo("jobject", "Object", "jobject", false, "Generic Java object"));
        addType(new JNITypeInfo("jclass", "Class<?>", "jclass", false, "Java class reference"));
        addType(new JNITypeInfo("jstring", "String", "jstring", false, "UTF-16 Java string"));
        addType(new JNITypeInfo("jthrowable", "Throwable", "jthrowable", false, "Java exception"));
        addType(new JNITypeInfo("jobjectArray", "Object[]", "jobjectArray", true, "Array of Java objects"));

        //
        addType(new JNITypeInfo("jweak", "WeakReference<?>", "jweak", false, "Weak global reference"));
        addType(new JNITypeInfo("jvalue", "Object (union)", "jvalue", false, "Union for JNI argument values"));

        //
        addType(new JNITypeInfo("JNIEnv", "JNIEnv*", "JNIEnv*", false, "JNI environment pointer"));
        addType(new JNITypeInfo("JavaVM", "JavaVM*", "JavaVM*", false, "Java Virtual Machine interface pointer"));
        addType(new JNITypeInfo("jmethodID", "long", "jmethodID", false, "Method identifier"));
        addType(new JNITypeInfo("jfieldID", "long", "jfieldID", false, "Field identifier"));

        //
        addType(new JNITypeInfo("JNIEXPORT", "", "JNIEXPORT", false, "JNI export specifier (macro)"));
        addType(new JNITypeInfo("JNICALL", "", "JNICALL", false, "JNI call specifier (macro)"));

        //
        addType(new JNITypeInfo("jsize", "int", "jsize", false, "Size type used by JNI (32-bit signed integer)"));
        addType(new JNITypeInfo("jbooleanRef", "boolean*", "jboolean*", false, "Pointer to boolean value"));
    }

    //
    public static void addType(JNITypeInfo info) {
        typeMap.put(info.getJniName(), info);
    }

    //
    public static JNITypeInfo getType(String jniName) {
        return typeMap.get(jniName);
    }

    //
    public static boolean isJNIType(String name) {
        return typeMap.containsKey(name);
    }

    //
    public static Collection<JNITypeInfo> getAllTypes() {
        return typeMap.values();
    }
}
