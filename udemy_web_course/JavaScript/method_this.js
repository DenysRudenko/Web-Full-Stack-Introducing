var carSeller1 = {
    firstName: "Jack",
    lastName: "White",
    regYear: 2017,
    hasDiscount: true,
    discount: 0,
    calculateDiscount: function (year) {
        var discount;
        var numberOfYears = 2019 - this.regYear;
        if ((numberOfYears) <= 2) {
            discount = 0;
        } else if((numberOfYears > 2) &&
        (numberOfYears <= 5)) {
            discount = 20;
        } else if (numberOfYears > 2) {
            discount = 30;
        }
        return discount;
    }
}

var discount = carSeller1.calculateDiscount();
carSeller1.discount = discount;

console.log(carSeller1);