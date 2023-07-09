class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        points = 0
        total_calories = 0
        
        for i, calorie in enumerate(calories):
            total_calories += calorie
            
            if i >= k - 1:
                if total_calories < lower:
                    points -= 1
                elif total_calories > upper:
                    points += 1
                
                total_calories -= calories[i - k + 1]
        
        return points
