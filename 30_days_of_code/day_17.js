//Write your code here

class Calculator {
    power(n, p) {
        try {
            if (n < 0 || p < 0) {
                return 'n and p should be non-negative';
            }
            else {
                return n ** p;
            }
        } catch (err) {
            return;
        }
    }
}

