// let marks_ = [91,82,63,84,"A",false]
// array.forEach(element => {
    
// });(let i = 0; i < arr.length; i++) {
//     console.log()
// }
// console.log(marks_)
// console.log(marks_[4])
// console.log(marks_.length)
// console.log(typeof marks_)
// //toString
// let c = marks_.join("_")
// console.log(c) 
//shift
//unshift
//delete
//concat

// let str = 'Bumi/"'
// let str1 = "kali"
// console.log(str.toLowerCase)
// console.log(str.slice(2,4))
// console.log(str.replace("Bu","ub"))
// console.log(str.concat("- advanced ",str1," ok"))
//trim

// let marks_ = [1,3.4,false,345,9078]
// let ane = "gnome"
// let arr = Array.from(ane)
// console.log(arr)

// let a = arr.map((value,index,array) => {
//     console.log(value,index,array) 
//     return value + index})
// console.log(a)

// //array filter method .................... doesn't change the original array
// let arr2 = [1,2,7,'false',4.09]
// let a2 = arr2.filter((val) => {
//     return val < 3})
//     console.log(a2)

// //reduce
// let arr3 = [1,2,3,4,45,5]
// let a3 = arr3.reduce((a,b) =>{
//     return a+b
// })
// console.log(a3)

// console.assert()
// console.clear()
// console.warn()
// console.table()      //=> obj
// console.timeEnd()
// alert("Your Script works")
// let a4 = prompt("enter the value:")
// a4 = Number.parseInt(a4)
//let confirm = confirm("Do yoyu write on the page? ")
// if(confirm)
// {document.write(a4)}

//for....of
// for(let it of marks_)
// {
//     console.log(it)
// }


// //for....in
// for(let i in marks_)
// {
//     console.log(i)
// }



// marks_.forEach((element) => {
//     console.log(element*element)
// })

//html collection,DOM - document obj model
//BOM - document obj model
// window.console.log(a)  --> global
// console.log(document.body)
// document.body.background = "yellow"

// g ... s = win
// w ... g = win
// s ... w = win
 

// do{

//     // let num = prompt("Enter number: ")
//     // // let runAgain = true
//     let num = prompt("Enter any one (S as snake , W as water , G as Gun): ")
//     let runAgain = true
//     const charecters = ['S','W','G']
//     const ri = Math.floor(Math.random() * characters.length);
//     const rc = charecters[ri];

//     const win = (num,rc) =>{
//        if(num ==  "S" && rc == "W")           return true;
//        if(num ==  "W" && rc == "G")           return true;
//        if(num ==  "S" && rc == "W")           return true;
//        else                                   return false;
//     }

//     if(win(num,rc))
//     {
//         alert("Win Win Win")
//     }
//     else{
//         alert("You fucked the game !")
//     }
    // num = Number.parseInt(num)
    // // if(num < 4)
    // // {
    // //     location.href = "https://github.com"
    // // }
    // if(num > 59)
    // {
    //     console.error("Invalid Number")
    // }
    // const canDrive = (num) =>{
    // return num > 0 ? true : false
    // }
    // if(canDrive(num))
    // {
    //     alert("Positive")
    // }
    // else{
    //     alert("Non-Positive")
    // }
//     runAgain = confirm("Do you want to try your luck once gain?")

//     // let color = prompt("Enter Background Color: ")
//     // document.body.style  = color;
// }while(runAgain);

// WALKING THE DOM

// document.getElementsByClassName("")[3].color = "Red"

// DOM TreeWalker
// document->html->Headers,body
// text nodes
// ele nodes
// comment nodes
// autocorrection

// console.log(document.body.firstChild)

// Element.firstChild
// Element.childNodes
// child nodes aren't arrays

//$0 - recently accessed ele, $1 - prev recrently acceseed ele
//parent ele,parent node

//Searching the DOM
//document.getElementbyId()
//document.querySelectorAll("child-title")
//document.getElementsByClassName("")[3].color = "Red"

//console.log(id1.matches('.box')
//console.log(id1.closest('.box')
//console.log(id1.contains('.box')

// let a = document.getElementById("fir").getAttribute("class");
// console.log(a);

// console.log(first.hasAttribute("class"))
// first.setAttribute("hidden", "true");
// removeAttribute("hidden");


// we can make custom attributes
// console.log(fir.dataset)


// insertion methods
// let a = document.getElementsByTagName['div'][0]

// a.innerHTML = a.innerHTML + "<h1>Bonda</h1>"

// let newdiv = document.createElement('div');
// newdiv.innerHTML = "<h1>heading 1<h1/>"




// const btn = document.getElementById('btn');

// let x = function(event)
// {
//     console.log(event.target.value);
//     console.log(event,event.clientX,event.clientY);
//     // alert('Hello World1 !');
// };

// let y = function(e)
// {
//     // alert('Hello World2 !');
// };

// btn.addEventListener('click', x);
// btn.addEventListener('click', y);

// let a = prompt('Provide your favorite no. (1/2) :');

// if(a == 2)
// {
//     btn.removeEventListener('click',x)
// }

// if(a == 1)
// {
//     btn.removeEventListener('click',y)
// }

//callback
// function loadScript(url,callback) {
//     var script = document.createElement('script'); 
//     script.src = url; 
//     script.onload = function() { 
//         console.log("SRC : " + url);
//         callback(null,url);
//     }
//     script.onerror = function() {
//         console.log("Error loading script with SRC : " + url);
//         callback(new Error("Src got some error"))
//     }
//     document.body.appendChild(script); 
// }

// function hello(error,url)
// {
//     if(error)
//     {
//         console.log("error")
//         sendEmergencyMessageToCeo();
//         return;
//     }
//     alert("Hello!" + url);
// }

// loadScript("https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",hello)
//{/* <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script> */}

//alert in node.js print to console

//promise

// let p1 = new Promise(function(resolve, reject) {
//     setTimeout(function() {
//         console.log("Hello 1!");
//         reject(new Error("I am an error"));
//         // resolve(true);
//     }, 3000);
// });

// let p2 = new Promise(function(resolve, reject) {
//     setTimeout(function() {
//         console.log("Hello 2!");
//         reject(new Error("I am an error")); // Uncomment this line to trigger the error
//         // resolve(true);
//     }, 3000);
// });

// p1
//     .then((value) => {
//         console.log(value);
//     })
//     .catch((error) => {
//         console.log("Some error occurred on P1:", error);
//     });

// p2
//     .then((value) => {
//         console.log(value);
//     })
//     .catch((error) => {
//         console.log("Some error occurred on P2:", error);
//     });

//Promise Chaining

// p2.then((value)=>{
//     console.log(value);
// })

// console.log("hello 1!")
// setTimeout(function(){
//     console.log("Hello 2!")
// },3000)

// console.log("Hello3 !")
// console.log(p1,p2)

// [[PromiseState]] : "fulfilled"
// [[PromiseResult]] : 56

//fetch google.com
//fetch  data from API
//rest of he JS

//Promise Chaining
// let p1 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         console.log("Resolve after 2 secs")
//         resolve(45)
//     },2000)
// })

// p1.then((value) => {
//     console.log(value)
//     let p2 = new Promise((resolve, reject) => {
//        setTimeout(() => {resolve("Promise 2")},2000)  
//     })
//     return p2
// }).then((value) => {
//     console.log("We are done")
//     return 2;
// }).then((value) => {
//     console.log("We are pakka done done")
//     return 2;
// })

// function loadScript(url,callback)
// {
//     return new Promise((resolve,reject) =>
//     {
//         var script = document.createElement("script");
//         script.src = url;
//         script.onload = () =>{
//            resolve(1); 
//         }
//         script.onerror = function() {
//             reject(0);
//         }
//         document.body.appendChild(script);
//     })
// }

// function hello(error,url)
// {
//     if(error)
//     {
//         console.log("error")
//         sendEmergencyMessageToCeo();
//         return;
//     }
//     alert("Hello!" + url);
// }

// let p1 = loadScript("https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js",hello)

// p1.then((value) => {
//     console.log(value);
// }).then((value) => {
//     console.log("Second Script is ready Sir");
// }).catch((error => {
//     console.log("Error is there")
// }))

//attaching more than one handlers

// let p = new Promise((resolve, reject) => {
//     alert("Hey I am resolved")
//     setTimeout(()=>{
//         resolve(1);
//     },2000)
// })
// p.then (()=>{
//     console.log("Hurray!")
// })
// p.then(()=>{
//     console.log("Promise is now resolved")
// })


//Promise API
// let p1 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve("Value 1")
//     },1000)
// })
// let p2 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         // resolve("Value 2")
//         reject(new Error("Error"));
//     },2000)
// })
// let p3 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve("Value 3")
//     },3000)
// })


// let promise_all = Promise.allSettled([p1,p2,p3])
// promise_all.then((value) =>{
//     console.log(value)
// });

// let promise_all = Promise.allS([p1,p2,p3])
// promise_all.then((value) =>{
//     console.log(value)
// });

// let promise_all = Promise.any([p1,p2,p3])
// promise_all.then((value) =>{
//     console.log(value)
// });

// let promise_all = Promise.allSettled([p1,p2,p3])
// promise_all.then((value) =>{
//     console.log(value)
// });
//if we print all the data at the same time , 
// then we can print p3 value along with the former two , 
// but in real world , the the values are random we have to use the PROMISE API

// async function f() {
//     let delhiW = new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve("27 Deg");
//         }, 1000);
//     });
//     let bangaloreiW = new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve("39 Deg");
//         }, 2000);
//     });

//     let delhiWe = await delhiW;
//     let bangaloreWe = await bangaloreiW;
//     return [delhiWe, bangaloreWe];
// }

// f()
// .then((a) => {
//     console.log(a);
// })
// .catch((error) => {
//     console.error(error);
// });


// //Errror obj
// try{
//     //customError
//     throw new Error("Dev is not Good")
//     console.log(value)
// }
// catch(error)
// {
//     console.log(error.name)
//     console.log(error.message)
//     console.log(error.stack)
// }
// //we acnnot add setTimeOut in try-catch as it works asynchronously
// //finally clause
// finally{
//     console.log()   //hamesa challega if catch ke andar error aaega
// }


//FETCH API
// let p = fetch("https://anime-facts-rest-api.herokuapp.com/api/v1/fma_brotherhood")
// p.then((value1)=>{
//     console.log(value1.status)
//     console.log(value1.ok)
//     return value1.json();
// }).then((value2)=>{
//     console.log(value2.status)
//     return value2;
// })

// let proxyUrl = 'https://cors-anywhere.herokuapp.com/';
// let apiUrl = 'https://anime-facts-rest-api.herokuapp.com/api/v1/fma_brotherhood';

// fetch(proxyUrl + apiUrl)
//     .then((response) => {
//         return response.json();
//     })
//     .then((data) => {
//         console.log(data);
//     })
//     .catch((error) => {
//         console.error(error);
//     });

// let proxyUrl = 'https://cors-anywhere.herokuapp.com/';
// let apiUrl = 'https://anime-facts-rest-api.herokuapp.com/api/v1/fma_brotherhood';

// // Send a request to the CORS proxy
// fetch(proxyUrl + apiUrl)
//     .then((response) => {
//         return response.json();
//     })
//     .then((data) => {
//         console.log(data);
//     })
//     .catch((error) => {
//         console.error(error);
//     });

//we cannot execute response.text()and response.json() at same time


//Sending POST with Fetch API
// const createTodo = async () => {
//         let options = {
//         method: "POST",
//         headers:{"Content-type": "application/json"}
//     },

    
//     body: JSON.stringify({
//         title: 'foo',
//         body: 'bar',
//         userId: 1,
// })
//     let p = await fetch('https://jsonplaceholder.typicode.com/posts',options)
//     let response = p.json()
//     return response
// }
// const mainFunc = () => {
//     let todo = createTodo()
//     console.log(todo)
// }

// mainFunc()
// fetch(url, options)
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.error(error));
  //json.string -> json obj convert to string
  //json.parse -> valid json string convert to js obj

//   const createTodo = async () => {
//     let options = {
//         method: "POST",
//         headers: { "Content-type": "application/json" },
//         body: JSON.stringify({
//             title: 'foo',
//             body: 'bar',
//             userId: 1,
//         })
//     };

//     try {
//         let response = await fetch('https://jsonplaceholder.typicode.com/posts', options);
//         let todo = await response.json();
//         return todo;
//     } catch (error) {
//         console.error(error);
//         throw error; // Re-throw the error for handling in the caller
//     }
// }

// const getTodo = async (id) => {
//     try {
//         let response = await fetch('https://jsonplaceholder.typicode.com/posts/' + id);
//         let todo = await response.json();
//         return todo;
//     } catch (error) {
//         console.error(error);
//         throw error;
//     }
// }

// const mainFunc = async () => {
//     try {
//         let createdTodo = await createTodo();
//         console.log("Created Todo:", createdTodo);

//         let todoId = createdTodo.id;
//         let retrievedTodo = await getTodo(todoId);
//         console.log("Retrieved Todo:", retrievedTodo);
//     } catch (error) {
//         console.error(error);
//     }
// }

// mainFunc();

//cookies in JavaScript - store data in browsers
//cookie coder HTTP header
//futher declaration of custom cookies add it not replace it with previous cookies
//exact no. i sdecidede by browsers

//let key = prompt("Enter your Key : ")
//let Value = prompt("Enter your Value : ")
// document.cookie = $(encodeURIComponent(key)) = $(encodeURIComponent(value))
// console.log(document.cookie)

//Localstorage
//Har request pe nahi bheja jaega as in cookies
//broser restart or pag e refresh , the data never disappears
// localStorage.setItem("Name ","Devas")
//getItem,removeItem,localStorage.key(0)

//SessionStorage - same methods, ek samya tak Jiwit