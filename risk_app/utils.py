"""
Manages loading the saved scikit-learn model and making predictions.

This module uses a simple caching mechanism (`_cached`) to avoid
re-loading the model from disk on every prediction request.
"""

import joblib
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, Union

# Define the path to the model file relative to the project root
MODEL_PATH = Path(__file__).resolve().parent.parent / 'models/saved_model.joblib'

# In-memory cache for the model bundle (model + features list)
_cached_model_bundle: Optional[Dict[str, Any]] = None


def load_model() -> Dict[str, Any]:
    """
    Loads the model bundle from the file system into the cache.
    
    If the model is already in the cache (`_cached_model_bundle`),
    it returns the cached version directly.
    
    Raises:
        FileNotFoundError: If the model file does not exist at MODEL_PATH.
        
    Returns:
        Dict[str, Any]: The loaded model bundle, typically containing
                        {'model': <model_object>, 'features': <list_of_features>}.
    """
    global _cached_model_bundle
    
    # Return from cache if already loaded
    if _cached_model_bundle is not None:
        return _cached_model_bundle

    # Check if the model file exists before trying to load
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. "
            "Ensure the model is trained and saved in the correct location."
        )

    print(f"Loading model from {MODEL_PATH}...")
    _cached_model_bundle = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
    return _cached_model_bundle


def predict_from_dict(data: Dict[str, Union[int, float]]) -> Tuple[int, Optional[float]]:
    """
    Generates a risk prediction from a dictionary of input features.
    
    Args:
        data (Dict): A dictionary where keys are feature names
                    (e.g., 'income', 'age') and values are the
                    corresponding input values.
                    
    Returns:
        Tuple[int, Optional[float]]: A tuple containing:
            - The predicted label (int, e.g., 0 or 1).
            - The prediction
            """