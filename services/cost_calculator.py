def calculate_cost(model_name,tokens):
     
     pricing={
        "gpt-4o-mini": 0.00000015,
        "gpt-4o": 0.000005
     }

     price_per_token=pricing.get(model_name,0.000005)

     return round(tokens*price_per_token,6)

