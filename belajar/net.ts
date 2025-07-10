import * as net from "node:net";
import * as http from "node:http";

const server = {
	http: http.createServer((req, res) => {
		return [req, res];
	}),
	net: net.createServer((socket) => {
		socket.write("lawak");
	}),
};
