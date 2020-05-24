import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'


// 子コンポーネント
// class Square extends React.Component {
//   // コンストラクタを追加してstateを初期化
//   // これでコンポーネントが状態を持てるようになるよ
//   // とはいえ状態を持つのは親にさせた方が都合がいいので消します
//   // constructor(props) {
//   //   super(props);
//   //   this.state = {
//   //     value: null,
//   //   };
//   // }


//     render() {
//       return (
//         // functionじゃなくてアロー関数で書けるけどonClickに渡すのは関数なので注意
//         // <button className="square" onClick={function() {alert:'clickしたよ'}}>
//         // <button className="square" onClick={() => alert('clickしたよ')}>
//         //   {this.state.value}
//         // </button>
//         <button
//           className="square"
//           onClick={() => this.props.onClick()}
//         >
//           {this.props.value}
//         </button>
//       );
//     }
//   }

  // Squareコンポーネントをシンプルに書き換えるよ
  function Square(props) {
    return (
      <button className="square" onClick={props.onClick}>
        {props.value}
      </button>
    )
  }

  // 親コンポーネント
  class Board extends React.Component {
    // やっぱり状態は親コンポーネントで持ってたほうが都合がいいよねということでリファクタリング(stateをリフトアップ)
    // Gameコンポーネントに状態を持たせるためにここもリファクタリングで消します(Stateをリフトアップ)
    // constructor(props) {
    //   super(props);
    //   this.state = {
    //     squares: Array(9).fill(null),
    //     xIsNext: true,
    //   };
    // }

    renderSquare(i) {
      return (
        <Square
          value={this.props.squares[i]}
          onClick={() => this.props.onClick(i)}
        />
      );
    }

    render() {
      // ここの処理は親コンポーネントのGameに処理が移動したのでここは不要になりました
      // const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
      // const winner = calculateWinner(this.state.squares);
      // let status;
      // if (winner) {
      //   status = 'Winner:' + winner;
      // } else {
      //   status = 'Next Player: ' + (this.state.xIsNext ? 'X' : 'O');
      // }

      return (
        <div>
          {/* <div className="status">{status}</div> */}
          <div className="board-row">
            {this.renderSquare(0)}
            {this.renderSquare(1)}
            {this.renderSquare(2)}
          </div>
          <div className="board-row">
            {this.renderSquare(3)}
            {this.renderSquare(4)}
            {this.renderSquare(5)}
          </div>
          <div className="board-row">
            {this.renderSquare(6)}
            {this.renderSquare(7)}
            {this.renderSquare(8)}
          </div>
        </div>
      );
    }
  }
// 親の親コンポーネント
  class Game extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        history: [{
          squares: Array(9).fill(null),
        }],
        stepNumber: 0,
        xIsNext: true,
      };
    }

    handleClick(i) {
      const history = this.state.history.slice(0, this.state.stepNumber + 1);
      const current = history[history.length - 1];
      const squares = current.squares.slice();
      if (calculateWinner(squares) || squares[i]) {
        return;
      }
      squares[i] = this.state.xIsNext ? 'X' : 'O';
      this.setState({
        // concatはもとの配列をミューテートしないのがよいのでpushではなくconcatしてるらしい
        history: history.concat([{
          squares: squares,
        }]),
        stepNumber: history.length,
        xIsNext: !this.state.xIsNext,
      });
    }

    jumpTo(step) {
      this.setState({
        stepNumber: step,
        xIsNext: (step % 2) === 0,
      });
    }

    render() {
      const history = this.state.history;
      const current = history[this.state.stepNumber];
      const winner = calculateWinner(current.squares);

      const moves = history.map((step, move) => {
        const desc = move ?
        'Go to move #' + move :
        'Go to game start';
        return (
          <li key={move}>
            <button onClick={() => this.jumpTo(move)}>{desc}</button>
          </li>
        );
      });

      let status;
      if (winner) {
        status = 'Winner: ' + winner;
      } else {
        status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
      }

      return (
        <div className="game">
          <div className="game-board">
            <Board
              squares={current.squares}
              onClick={(i) => this.handleClick(i)}
            />
          </div>
          <div className="game-info">
            <div>{status}</div>
            <ol>{moves}</ol>
          </div>
        </div>
      );
    }
  }

  function calculateWinner(squares) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }
    return null;
  }

  // ========================================

  ReactDOM.render(
    <Game />,
    document.getElementById('root')
  );
