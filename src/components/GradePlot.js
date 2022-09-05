import Plot from 'react-plotly.js';


const GradePlot = () => {
	const year = ["2020 Fall", "2021 Spring", "2021 Summer", "2021 Fall", "2022 Spring"];
	return (
		<div>
			<Plot
				data={[

					{
						name: "RITCHEY P",
						x: year,


						y: [3.082, 2.763, 2.868, 3.558, 2.674],
						type: 'scatter',
						mode: 'lines+markers',
						// marker: {color: 'red'},
					},

					{
						type: 'scatter',
						mode: 'lines+markers',
						x: year,
						y: [2, 5, 3]
					},

				]}

				layout={
					{
						width: 900,
						height: 600,
						title: 'Grade Distribution for: 121',
						xaxis: {
							title: 'year'
						},
						yaxis: {
							title: 'GPA'
						},
					}
				}
			/>
		</div>
	)
}

export default GradePlot;