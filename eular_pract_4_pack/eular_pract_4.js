function is_palindrome(val) {
    if (typeof val !== 'number') return '${val} is not a number';

    val = val.toString().split('');

    for (let i = 0; i < val.length; i++) {
        if (val[i] !== val[val.length - i - 1]) return false;
    }
    return true;
}

function largestPalindrome() {
    let highest = 0;

    for (let i = 999; i >= 100; i--) {
        for (let j = 999; j >= 100; j--) {
            let product = i * j;
            if (product < highest) break;
            console.log(product, i, j, highest, is_palindrome(product))
            if (is_palindrome(product) && product > highest) {
                highest = product;
            }
        }
    }
}