import { TextField } from "@material-ui/core";
import React, { Component, useState } from "react";

type Props = {
	value?: string;
}

interface State {
	userInput: string;
}

class Game extends React.Component<Props> {
	const [userInput: string, setUserInput: any] = useState<State>({userInput: 'hello'});
	constructor(props: Props) {
		super(props);
	}
	handleUserInput() {
		console.log(this.state.userInput);
	}
	render() {
		return (
			<TextField
				id="first-name"
				label="Input Wordle"
				value={}
				onChange={(e) => {
					this.setState({userInput: e.target.value});
				}}
				margin="normal"
			/>
		);
	}
}

export default Game;