package entity;

import java.io.Serializable;

public class JNITypeInfo implements Serializable {
    private String jniName;
    private String javaType;
    private String cppType;
    private boolean isArray;
    private String description;

    public JNITypeInfo(String jniName, String javaType, String cppType, boolean isArray, String description) {
        this.jniName = jniName;
        this.javaType = javaType;
        this.cppType = cppType;
        this.isArray = isArray;
        this.description = description;
    }

    // Getters / Setters
    public String getJniName() { return jniName; }
    public String getJavaType() { return javaType; }
    public String getCppType() { return cppType; }
    public boolean isArray() { return isArray; }
    public String getDescription() { return description; }

    @Override
    public String toString() {
        return String.format("JNITypeInfo[%s -> Java:%s, C++:%s, Array:%b]",
                jniName, javaType, cppType, isArray);
    }
}
