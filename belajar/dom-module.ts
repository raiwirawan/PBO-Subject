import { StringLiteral } from "typescript";

const dom = {
	select: (query: string) => {
		const elm = document.querySelector(query);
		// console.log(elm, " element selected");
		return elm;
	},
	clip: (element_clip_wrapper: Element, element_want_to_clip: Element) => {
		element_clip_wrapper.append(element_want_to_clip);
		console.log(
			element_want_to_clip,
			" has clipped into ",
			element_clip_wrapper
		);
	},
	create: (
		tag: string,
		attributes: {
			key: string;
		}
	) => {
		const created_elm = document.createElement(tag);

		for (const [key, value] of Object.entries(attributes)) {
			created_elm.setAttribute(key, value);
		}

		return created_elm;
	},
	inner: (target: Element, inner: string) => {
		target.innerHTML = inner;
	},
	set: (
		target_elm: Element | null,
		attribute_name: "class" | "name" | "data-name" | "type" | "id",
		value: string
	) => {
		target_elm?.setAttribute(attribute_name, value);
	},
	style: (options: {
		option: "add" | "delete";
		style: {
			key: string;
			value: string;
		};
		element: HTMLElement;
	}) => {
		const { option, style, element } = options || {};

		if (option === "add") {
			element.style[style.key] = style.value;
		} else if (option === "delete") {
			element.style[style.key] = "";
		}
	},
	class: (options: {
		element: Element | null;
		action: "add" | "remove";
		classes: string;
	}) => {
		const { element, action, classes } = options || {};

		if (action === "add") {
			element?.classList.add(classes);
		} else if (action === "remove") {
			element?.classList.remove(classes);
		} else {
			console.log("Invalid element or action or classes");
		}
	},
	generate: (config: {
		what: string;
		who: string;
		when: string;
		where: string;
		why: string;
		how: string;
	}) => {
		const { what, who, when, where, why, how } = config || {};

		return how;
	},
};

const main = dom.select("#main");
dom.set(main, "class", "main lawak ajg");
dom.class({
	element: main,
	action: "add",
	classes: "main relative w-full h-full",
});
