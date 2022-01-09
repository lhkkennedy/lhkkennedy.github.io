clear
import delimited using "C:\Users\lhkke\OneDrive - University of Bristol\Documents\Work\Year_3\Data_Science\Debt_Project\DeficitNet.csv"


reshape long @milliongdp, i(date) j(type) string

export delimited using "DeficitNet.csv", replace