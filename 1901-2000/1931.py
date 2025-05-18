class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        # Step 1: Generate all valid column colorings (no vertical conflicts)
        def generate_states(pos, prev_color, state):
            if pos == m:
                states.append(tuple(state))
                return
            for color in range(3):
                if color != prev_color:
                    state[pos] = color
                    generate_states(pos + 1, color, state)

        states = []
        generate_states(0, -1, [0] * m)
        index_map = {state: i for i, state in enumerate(states)}

        # Step 2: Precompute valid transitions (no horizontal conflicts)
        size = len(states)
        transitions = [[] for _ in range(size)]
        for i, a in enumerate(states):
            for j, b in enumerate(states):
                if all(x != y for x, y in zip(a, b)):
                    transitions[i].append(j)

        # Step 3: DP initialization
        dp = [1] * size

        # Step 4: DP iteration for each column
        for _ in range(1, n):
            new_dp = [0] * size
            for i in range(size):
                for j in transitions[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        # Step 5: Return total number of valid colorings
        return sum(dp) % MOD
