package mx.pepo.pattern.foster

class PhotoContainer {
    Integer idPhoto
    String name
    String hashPhoto
    Byte[] content
    String related
    String bluePercent
    String redPercent
    String greenPercent
    boolean hasEyes
    boolean hasNose
    boolean hasMouth
    Integer numberOfRectagles
    static constraints = {
        hashPhoto(unique: true)
    }
    static mapping = {
        version false
        id(name: "idPhoto",generator: "increment")
    }
}
