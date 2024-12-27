class Solution(object):
  def maxScoreSightseeingPair(self, values):
    max_score = 0
    score = values[0]
    for i in range(1, len(values)):
      score -= 1
      if (score + values[i] > max_score):
        max_score = score + values[i]
      if (values[i] > score):
        score = values[i]
    return max_score
        
