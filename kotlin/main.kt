import java.io.File
import java.io.FileReader


// rewrite to for loop. to length too
fun filereader() {
    var filename = File("client.dll")
    var pattern = "Maximum visible distance\\x00\\x00\\x00\\x00\\d{4}".toRegex()
    var readeable = filename.readText()
    var matches = pattern.find(readeable)
    var yourDistance = (matches!!.value)
    var view = yourDistance.slice(27..31)
    println("Your camera distance: $view")
}

fun main(args: Array<String>){
    println("Default camera distance: 1200")
    filereader()

}
