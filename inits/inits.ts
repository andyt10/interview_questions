

function inits<Type>(l: Array<Type>): Array<Array<Type>> {
    let retVal: Array<Array<Type>> = [[]];

    l.forEach((value,index) => {
        retVal.push(l.slice(0,index+1))
    })
    return retVal;
}

console.log(inits([4,3,2,1]))