class Hello extends React.Component 
{
    render()
    {
        return (
            <div>
                <h1>Hello {this.props.somename1}!</h1>
                <button onClick={this.handleClick}>Click Here</button>
            </div>
        );
    }

    handleClick = () => 
    {
        alert("Hi");
    }
}

class Counter extends React.Component 
{
    constructor(props) 
    {
        super(props);
        this.state = {
            count: 0,
            attr1: "bye"
        };
    }

    render() 
    {
        return (
        <div>
            <h1>{this.state.count}</h1>
            <button onClick={this.increment}>Increment</button>
            <button onClick={this.decrement}>Decrement</button>
        </div>
        );
    }

    increment = () => 
    {
        this.setState(oldstate => ({count: oldstate.count + 1}));
    }

    decrement = () => 
    {
        this.setState(oldstate =>({count: oldstate.count -1}));
    }
}

class Test extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = 
        {
            num1: 1,
            num2: 1,
            score: 0,
            response: "",
            incorrect: false
        };
    }

    render() 
    {
        if (this.state.score === 10)
        {
            return this.renderWin();
        }
        else
        {
            return this.renderProblem();
        }
    }

    renderWin() 
    {
        const name = "the addition game";
        return (<Winner name={name} />);
    }

    renderProblem()
    {
        return (
            <div>
                <div id="problem" className={this.state.incorrect ? "incorrect" : ""}>
                    {this.state.num1} + {this.state.num2}
                </div>
                <div>
                    <input onKeyPress={this.inputKeyPress} onChange={this.updateResponse} value={this,state.response} />
                    Current Guess is {this.state.response}
                </div>
                <div>
                    Score: {this.state.score}
                </div>
                <button onClick={this.resetGame}>Reset</button>
            </div>
        );
    
    }

    updateResponse = (event) => 
    {
        this.setState({ response: event.target.value });
    }

    inputKeyPress = (event) => 
    {
        if (event.key === "Enter") 
        {
            const answer = parseInt(this.state.response);
            if (answer === this.state.num1 + this.state.num2)
            {
                this.setState(state => ({
                    num1: Math.ceil(Math.random() * 10) + state.score,
                    num2: Math.ceil(Math.random() * 10) + state.score,
                    response: "",
                    incorrect: false,
                    score: state.score + 1
                }));
            }
            else
            {
                this.setState({response: "", incorrect: true});
            }
        }
    }

    resetGame = (event) => 
    {
        this.setState({num1: 1, num2: 1, response: "", incorrect: false, score: 0});
    }
}


class App extends React.Component 
{
    render() 
    {
        return (
            <div>
                <Hello somename1="Alice"></Hello>
                <Hello somename1="Bob" />
                <Counter />
                <Test />
            </div>
        );
    }
}

ReactDOM.render(<App />, document.querySelector("#app"));