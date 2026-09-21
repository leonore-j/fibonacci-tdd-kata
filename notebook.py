import marimo

__generated_with = "0.24.2"
app = marimo.App()


app._unparsable_cell(
    r"""
    def Fibonacci():
        '''
        Reminder: the Fibonacci sequence is defined by  
        F(0) = 0  
        F(1) = 1   
        F(n) = F(n−1) + F(n−2)    for n ≥ 2

        '''
    	pass
    """,
    name="*Fibonacci"
)


if __name__ == "__main__":
    app.run()
