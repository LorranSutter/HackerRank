function avg(arr) {
    let arrLength = arr.length;
    if (arrLength === 0) return 0;
    return arr.reduce((a, b) => a + b, 0) / arrLength;
}

class Student extends Person {
    /*	
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor here
    constructor(_firstName, _lastName, _id, _scores) {
        super(_firstName, _lastName, _id);
        this.scores = _scores;
    }

    /*	
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
    calculate() {
        let average = avg(this.scores);

        if (average >= 90) return 'O';
        if (average >= 80) return 'E';
        if (average >= 70) return 'A';
        if (average >= 55) return 'P';
        if (average >= 40) return 'D';
        return 'T';
    }

}

