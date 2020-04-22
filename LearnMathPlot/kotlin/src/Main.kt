//top level variable

//si agregamos un signo de interrogacion a la variable eso hace
//que el null sea aceptado como un string es como un casteo

//val no pueden tener un valor reasginado
//var si puede reasignar valor a la variable
val name: String? = null
var greeting: String? = null

fun main(){
    //greeting = "hello"

    //Le pasamos como parametro el value a evaluar
    //y hace switch para ir cambiando segun el valor que tenga
    when(greeting){

        //Si el valor es null imprime hi
        null -> println("Hi")
        //Si tiene otro valor imprime greeting
        else -> println(greeting)
    }
    //Esto es lo mismo pero escrito de otra forma
    val valuePrint = if(greeting != null) greeting else "hi"
    println(valuePrint)
    //otra forma de hacerlo
    val another = when (greeting){
        null -> "Hi"
        else -> greeting
    }
    println(another)
    println("********************************************************")
    println("BASIC FUNCTIONS")
    //Invocando funcion
    println(getter())
    sayHello()
    rata("Hello","David")
    println("********************************************************")
    println("ARRAYS Y CICLOS")
    //Declarando array
    val thing = arrayOf("Spiderman", "Programming", "Comic books")
    println(thing.size)
    //imprimir un termino
    println(thing[0])
    println(thing.get(0))
    //Interar sobre cada coso del array
    println("")
    for ( t in thing){
        println(t)
    }
    //Hace lo mismo pero con menos codigo
    //it es por default
    // para cambiarlo usamos t -> println(t)
    println("")
    thing.forEach{ t ->
        println(t)
    }
    println("")
    thing.forEachIndexed{index, t ->
        println("$t is at index $index")
    }
    println("")
    val box = listOf("Bugini","Stapler","RayoMcQueen")
    //Se accede a los elementos igual que ell array

    //Mutable signifca que podemos eliminar y agregar elementos
    val box2 = mutableListOf("cat")
    box2.add("Dog")

    //Using maps
    val map = mutableMapOf(1 to "a", 2 to "b", 3 to "c")
    //printing
    map.put(4,"d") //add element
    map.forEach {key , value -> println("$key -> $value")}

    println("")
    saying("Hi", box)

    println("********************************************************")
    println("Vararg, arguments y default parameter values")
    
}
//Define new function
//fun es para hacer saber que estamos definiendo una nueva funcion

fun getter(): String = "Hello motherfucker"

//Unit quiere decir que no retorna nada especial
fun sayHello() {
    println(getter())
}
/*
fun rata(item: String){
    //otro tipo de concatenacion
    val msg = "hello $item"
    println(msg)
}
 */
//otra forma de hacrlo
fun rata(great: String, item: String) = println("$great $item")

fun saying(great: String, item: List<String>){
    item.forEach {item ->
        println("$great $item")
    }
}