from contextlib import contextmanager

from sentence_transformers import SentenceTransformer


class RoutedSentenceTransformer:
    """
    SentenceTransformer wrapper that allows switching between document/query encoding with a context manager, used to accommodate asymmetric embedding models.
    Written with the help of Google Gemini.
    """

    def __init__(
        self,
        model: SentenceTransformer,
    ):
        self.model = model
        self._use_query_mode = False

    def encode(self, documents, show_progress_bar: bool = False, **kwargs):
        """
        BERTopic calls this method under the hood for both fitting/transforming
        and runtime queries. We inspect the active state and apply the appropriate prompt.
        """
        method = (
            self.model.encode_query
            if self._use_query_mode
            else self.model.encode_document
        )
        return method(
            documents,
            show_progress_bar=show_progress_bar,
            **kwargs,
        )

    @contextmanager
    def query_mode(self):
        """
        Context manager that temporarily toggles the encoder into query mode
        (e.g., applying search query prompts/prefixes) and safely resets on exit.
        """
        self._use_query_mode = True
        try:
            yield self
        finally:
            self._use_query_mode = False
