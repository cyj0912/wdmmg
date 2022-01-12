import os
from .app import app
from .csv import csv_to_dict
from .db import get_db
from .model import tx_from_bofa_credit_csv
from flask import render_template


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/accounts")
def accounts():
    return render_template("accounts.html")


@app.route("/donations")
def donations():
    return "<h1>This summarizes all your donations in the past year.</h1><p>For tax purposes.</p>"


@app.route("/setup")
def setup():
    db = get_db()
    # CREATE TABLE `Transaction` (
    # 	`posted_date` DATE,
    # 	`description` TEXT,
    # 	`amount` DECIMAL
    # );
    # CREATE TABLE `Account`
    # CREATE TABLE `Category`
    # CREATE TABLE `Merchant`
    return "<p>Setup</p>"


@app.route("/import")
def import_accounts():
    tx_list = []

    src_dir = "account_source"
    account_names = os.listdir(src_dir)
    for account_name in account_names:
        for src in os.listdir(src_dir + os.sep + account_name):
            fn = src_dir + os.sep + account_name + os.sep + src
            print(f"Importing {fn}")
            tx_list += csv_to_dict(fn)

    for tx in tx_list:
        tx_from_bofa_credit_csv(tx)

    return render_template("import.html", tx_list=tx_list)
