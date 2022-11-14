CREATE TABLE IF NOT EXISTS customer (
	id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	customer_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	price REAL NOT NULL,
	image_link TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
	id INTEGER PRIMARY KEY,
	customer_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	price REAL NOT NULL,
	quantity INTEGER NOT NULL,
	tps REAL NOT NULL,
	tvq REAL NOT NULL,
	discount REAL NOT NULL,
	total REAL NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customer(id),
	FOREIGN KEY (product_id) REFERENCES product(id)
);