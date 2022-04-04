var cars = [

    {
        carProduses: "mazda",
        carModel: "6",
        color: "red",
        year: 2017,
        isSelled: false
    },
    {
        carProduses: "mercedes",
        carModel: "c300",
        color: "grey",
        year: 2010,
        isSelled: true
    },
    {
        carProduses: "opel",
        carModel: "astra",
        color: "green",
        year: 2019,
        isSelled: true
    },
    {
        carProduses: "fial",
        carModel: "doblo",
        color: "white",
        year: 2011,
        isSelled: false
    }
]

/*for (var i = 0; i < cars.length; i++) {
    if (cars[i].isSelled === false) {
        console.log(cars[i]);
    }
}*/

cars.forEach(function(car) {
    if(car.isSelled === false) {
        console.log(car);
    }
})