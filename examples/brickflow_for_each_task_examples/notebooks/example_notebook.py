# Databricks notebook source

param = dbutils.widgets.get("looped_parameter")
print(f"Hey this is a nested notebook running with inputs: {param}")
