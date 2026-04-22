package models

import "fmt"

type Profile struct {
	PK             string   `json:"pk" dynamodbav:"pk"`
	SK             string   `json:"sk" dynamodbav:"sk"`
	Name           string   `json:"name" dynamodbav:"name"`
	Photo          string   `json:"photo" dynamodbav:"photo"`
	Addresses      []string `json:"addresses" dynamodbav:"addresses"`
	PaymentMethods []string `json:"paymentMethods" dynamodbav:"paymentMethods"`
}

func NewProfile(email string, name string, photo string) Profile {
	return Profile{
		PK:    fmt.Sprintf("USER#%s", email),
		SK:    "PROFILE",
		Name:  name,
		Photo: photo,
	}
}

type Order struct {
	PK      string `json:"pk" dynamodbav:"pk"`
	SK      string `json:"sk" dynamodbav:"sk"`
	Date    string `json:"date" dynamodbav:"date"`
	Address string `json:"address" dynamodbav:"address"`
	Total   int    `json:"total" dynamodbav:"total"`
	Status  string `json:"status" dynamodbav:"status"`
}

func NewOrder(email string, orderID string, date string, address string, total int) Order {
	return Order{
		PK:      fmt.Sprintf("USER#%s", email),
		SK:      fmt.Sprintf("ORDER#%s", orderID),
		Date:    date,
		Address: address,
		Total:   total,
		Status:  "pending",
	}
}

type Payment struct {
	PK     string `json:"pk" dynamodbav:"pk"`
	SK     string `json:"sk" dynamodbav:"sk"`
	Amount int    `json:"amount" dynamodbav:"amount"`
	Method string `json:"method" dynamodbav:"method"`
	Date   string `json:"date" dynamodbav:"date"`
	Status string `json:"status" dynamodbav:"status"`
}

func NewPayment(email string, orderID string, amount int, method string) Payment {
	return Payment{
		PK:     fmt.Sprintf("USER#%s", email),
		SK:     fmt.Sprintf("PAYMENT#%s", orderID),
		Amount: amount,
		Method: method,
		Date:   "",
		Status: "pending",
	}
}

type OrderHead struct {
	PK      string `json:"pk" dynamodbav:"pk"`
	SK      string `json:"sk" dynamodbav:"sk"`
	Date    string `json:"date" dynamodbav:"date"`
	Address string `json:"address" dynamodbav:"address"`
	Total   int    `json:"total" dynamodbav:"total"`
	Status  string `json:"status" dynamodbav:"status"`
}

func NewOrderHead(orderID string, date string, address string, total int) OrderHead {
	return OrderHead{
		PK:      fmt.Sprintf("ORDER#%s", orderID),
		SK:      "HEAD",
		Date:    date,
		Address: address,
		Total:   total,
		Status:  "pending",
	}
}

type OrderItem struct {
	PK       string `json:"pk" dynamodbav:"pk"`
	SK       string `json:"sk" dynamodbav:"sk"`
	Quantity int    `json:"quantity" dynamodbav:"quantity"`
	Price    int    `json:"price" dynamodbav:"price"`
	Subtotal int    `json:"subtotal" dynamodbav:"subtotal"`
}

func NewOrderItem(orderID string, productName string, quantity int, price int) OrderItem {
	return OrderItem{
		PK:       fmt.Sprintf("ORDER#%s", orderID),
		SK:       fmt.Sprintf("ITEM#%s", productName),
		Quantity: quantity,
		Price:    price,
		Subtotal: quantity * price,
	}
}
