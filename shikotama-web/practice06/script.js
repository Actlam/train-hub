array = [
    {name: 'kenji', mail:'fafa@eee.com'},
    {name: 'morita', mail: 'kkk@faf.com'}
    ]


// for (const key in array) {
//     console.log(key)
//     console.log(array[key].name)
//     console.log(array[key].mail)
//     mail_AA = [array[key].mail]
// }

arrayAA = []

for (const key of array) {
    arrayAA.push (array[key].mail);
}

console.log(arrayAA)