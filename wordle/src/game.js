import { TextField, Button } from "@material-ui/core";
import React, { Component, useState } from "react";



class Game extends React.Component {
	// Create state 

	wild_letters = new Map();
	set_letters = new Map();
	bad_letters = [];
	constructor(props) {
		super(props);
		this.state = { userInputGreen: "", userInputYellow: "", userInputGray: "" };
	}


	handleUserInput() {
		for (let i = 0; i < this.state.userInputGreen.length; i++) {
			let letter = this.state.userInputGreen.charAt(i);
			// If the letter is not "_"
			if (letter !== "_") {
				this.set_letters.set(i, letter);
			}
		}
		for (let i = 0; i < this.state.userInputYellow.length; i++) {
			let letter = this.state.userInputYellow.charAt(i);
			// If the letter is not "_"
			if (letter !== "_") {
				this.wild_letters.set(letter, i);
			}
		}
		for (let i = 0; i < this.state.userInputGray.length; i++) {
			let letter = this.state.userInputGray.charAt(i);
			// If the letter is not "_"
			if (letter !== "_") {
				this.bad_letters.push(letter);
			}
		}
		console.log(this.set_letters);
		console.log(this.wild_letters);
		console.log(this.bad_letters);
	}
	render() {
		return (
			<div>
				<TextField
					id="first-name"
					label="Green"
					value={this.state.userInputGreen}
					onChange={(e) => {
						this.setState({ userInputGreen: e.target.value });
					}}
					margin="normal"
				/>
				<TextField
					id="first-name"
					label="Yellow"
					value={this.state.userInputYellow}
					onChange={(e) => {
						this.setState({ userInputYellow: e.target.value });
					}}
					margin="normal"
				/>
				<TextField
					id="first-name"
					label="Gray"
					value={this.state.userInputGray}
					onChange={(e) => {
						this.setState({ userInputGray: e.target.value });
					}}
					margin="normal"
				/>
				<Button onClick={() => this.handleUserInput()}>Submit</Button>
			</div>


		);
	}
}

export default Game;