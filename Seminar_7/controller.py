import UI
import math_operation

def FunctionDefinition(operator):
    if operator == 'сложения': return math_operation.Addition()
    elif operator == 'вычитания': return math_operation.Subtraction()
    elif operator == 'умножения': return math_operation.Multiplication()
    elif operator == 'деления': return math_operation.Division()
    elif operator == 'получения остатка': return math_operation.Remains()
    else: return math_operation.Exponentiation()

def Сalculation():
    x,y,type = UI.GetData()
    math_operation.Init(x,y)
    resultCalculation = FunctionDefinition(type)
    UI.PrintResult(type, resultCalculation)