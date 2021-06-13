function inits(l) {
    var retVal = [[]];
    l.forEach(function (value, index) {
        retVal.push(l.slice(0, index + 1));
    });
    return retVal;
}
console.log(inits([4, 3, 2, 1]));
