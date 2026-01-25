import net, { Socket } from "node:net";
import http from "node:http";
import stream from "node:stream";

const http_server = http.createServer((req, res) => {
	console.log(req, res);
});

const net_server = net.createServer(
	{
		noDelay: true,
		allowHalfOpen: true,
		keepAlive: true,
		keepAliveInitialDelay: 1,
	},
	(sock) => {
		console.log(sock);
	}
);

const net_connection = net.createConnection({ port: 8124 }, () => {
	console.log("connected to server!");
	net_connection.write("world!\r\n");
});

net_connection.on("data", (data) => {
	console.log(data.toString());
	net_connection.end();
});

net_connection.on("end", () => {
	console.log("disconnected from server");
});
