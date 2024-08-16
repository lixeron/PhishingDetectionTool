def extract_features(parsed_email):
    features = {}
    features['url_count'] = len(parsed_email['urls'])
    suspicious_phrases = ['urgent', 'required immediately', 'at risk', 'verify your account', 'update your password']
    features['suspicious_phrase_count'] = sum(1 for phrase in suspicious_phrases if phrase in parsed_email['body'].lower())
    
    # Add more features based on your analysis and what was used during training
    return [features['url_count'], features['suspicious_phrase_count']]  # This should match the training feature set
