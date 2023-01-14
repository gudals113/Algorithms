// function asyncFunc1(value, cb){
//     setTimeout(()=>{
//         console.log(value+'th callback')
//         cb()
//     },0)
// }

// console.log('asyncFunc1 code start')

// asyncFunc1("1", ()=>{
//     asyncFunc1("2", ()=>{
//         asyncFunc1("3", ()=>{
//             asyncFunc1("4", ()=>{

//             })
//         })
//     })
// })
// console.log('asyncFunc1 code end')

// console.log('asyncFunc2 code start')
// function asyncFunc21(value) {
//     return new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             console.log(value+'th callback')
//             resolve("result")
//         })
//     },0)
// }
// function asyncFunc22(value) {
//     return new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             console.log(value+'th callback')
//             resolve()
//         })
//     })
// }

function asyncFunc23(value) {
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log(value+'th callback')
            resolve([1,2,3])
        })
    })
}

// asyncFunc21(1)
// .then((result)=> console.log(result,'here'),asyncFunc22(2))
// .then(asyncFunc23(3))qœq
// .catch((err)=>console.log(err))


// console.log('asyncFunc2 code end')


async function asyncFunc3() {
    const options = {method: 'GET', headers: {accept: 'application/json'}};
    const marketCode = await fetch('https://api.upbit.com/v1/market/all?isDetails=false', options)
    const jsonCode = await marketCode.json()
    
    console.log('Hello')
    console.log(jsonCode[0])


}

console.log('asyncFunc3 code start')
asyncFunc3()
console.log('asyncFunc3 code end')


function marry(man, woman) {
    woman.husband = man;
    man.wife = woman;
  
    return {
      father: man,
      mother: woman
    }
  }
  
let family = marry({name: "John"}, {name: "Ann"});