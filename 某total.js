//aHR0cHM6Ly93d3cudmlydXN0b3RhbC5jb20vZ3VpL2hvbWUvc2VhcmNo
function computeAntiAbuseHeader() {
    const e = Date.now() / 1e3;
    return btoa(`${(() => {
            const e = 1e10 * (1 + Math.random() % 5e4);
            return e < 50 ? "-1" : e.toFixed(0)
        }
    )()}-ZG9udCBiZSBldmls-${e}`)
}

console.log(computeAntiAbuseHeader())
