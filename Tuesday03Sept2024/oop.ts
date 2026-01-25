const fetchData = async (data_url: string) => {
	const response = await fetch(data_url);
	const json = response.json();
	return json;
};

const consoleData = async (data_url: string) => {
	console.log(await fetchData(data_url));
};

(async function () {
	await consoleData("https://jsonplaceholder.typicode.com/users");
})();
