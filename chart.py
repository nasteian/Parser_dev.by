import matplotlib.pyplot as plt
import numpy as np

def create_chart(data):
    plt.bar(["Удаленно","В офисе"],data)
    plt.ylabel('Y amount')
    plt.xlabel('X type')
    # plt.xticks(rotation=90)
    plt.savefig('saved.png')

