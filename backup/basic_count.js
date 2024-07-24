let in_count = 13;
let in_hold = 13;
let out_count = 13;
let out_hold = 13;

console.log("this works")
let run_count = function(in_count,in_hold,out_count,out_hold) {
    for(let i = 0; i < in_count; i ++) {
        print(i)
        
    }
} 

let testfunction = function() {
    print("works")
    // Example usage:
    pause(() =>  2);
}

function pause(callback, seconds) {
    setTimeout(callback, seconds * 1000);
}


