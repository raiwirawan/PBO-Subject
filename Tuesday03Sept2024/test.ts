interface CarInterface {
	car_name: string;
	car_type: string;
}

abstract class Car implements CarInterface {
	car_name: string = "Honda Jazz";
	car_type: string = "SUV";

	constructor() {}

	printCar() {
		return [this.car_name, this.car_type];
	}
}

class Peugeot extends Car {
	car_name: string = "Peugeot Regine";
	car_type: string = "Sportcar";

	constructor() {
		super();
	}

	printCar(): string[] {
		return [this.car_name, this.car_type];
	}
}

const peugeot = new Peugeot();

console.log(peugeot.printCar());
