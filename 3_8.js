function bubb(arr) {
    let swap;
    do {
    swap = false;
    for (let i = 1; i < arr.length; ++i) {
    if (arr[i - 1] > arr[i]) {
        [arr[i], arr[i - 1]] = [arr[i - 1],arr[i]];
        swap = true;
            }
        }
    }  
    while (swap)
    return arr
}
console.log(bubb([2, 324, 3, 20]));
