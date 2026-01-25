const myObj = {
	id: "Rama",
	age: 23,
};

const { id, age } = myObj;

const myElements = {
	header: document.querySelector("#header"),
	main: document.querySelector("#main"),
	footer: document.querySelector("#footer"),
};

const { header, main, footer } = myElements;

const listOfFn = {
	select: (query) => {
		const selectedElm = document.querySelector(query);
		console.log(selectedElm, " is selected!");
		return selectedElm;
	},
	clip: (wrapper, inner) => {
		wrapper.appendChild(inner);
		console.log(
			"Successfully merging ",
			wrapper,
			" as WRAPPER and ",
			inner,
			" as INNER"
		);
	},
	text: (txt, elm) => {
		elm.textContent = txt;
	},
	create: (tag, attributes) => {
		const created_elm = document.createElement(tag);

		for (const [key, value] of Object.entries(attributes)) {
			created_elm.setAttribute(key, value);
		}

		return created_elm;
	},
	inject: (target, object) => {
		target.append(object);
	},
};

const lof = listOfFn;

const wrapper = lof.select("#main");
const inner = lof.select("#footer");
const head = lof.select("#header");

lof.text("lawak kau ajg", wrapper);

const div_class_unified = lof.create("div", {
	class: "lawak ajg bangsat elek ngentot",
});

lof.clip(inner, div_class_unified);

const lawak = lof.select(".lawak");

lof.text("ajg kau", lawak);

lof.inject(wrapper, inner);
