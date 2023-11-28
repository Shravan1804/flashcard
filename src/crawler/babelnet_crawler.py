import babelnet as bn
from babelnet.data.source import BabelSenseSource
from babelnet.synset import SynsetType


class BabelNetCrawler:
    def clean_synsets(self, synsets):
        cleaned = synsets
        if any([s.is_key_concept for s in cleaned]):
            cleaned = [s for s in cleaned if s.is_key_concept]
        if any([s.type == SynsetType.CONCEPT for s in cleaned]):
            cleaned = [s for s in cleaned if s.type == SynsetType.CONCEPT]
        return cleaned

    def retrieve_synsets(self, concept, language):
        synsets = bn.get_synsets(
            concept,
            from_langs=[language],
            to_langs=[language],
            sources=[BabelSenseSource.WIKI, BabelSenseSource.WIKT],
        )
        return self.clean_synsets(synsets)

    def extract_flashcard_info(self, synset):
        definitions = synset.glosses
        examples = synset.examples()
        definition = definitions[0].gloss if definitions else None
        example = examples[0].example if examples else None
        image = synset.main_image.url if synset.main_image else None
        return definition, example, image

    def select_flashcard_info(self, flashcard_info_lst):
        for flashcard_info in flashcard_info_lst:
            if flashcard_info[0] and flashcard_info[1] and flashcard_info[2]:
                return flashcard_info
        return flashcard_info_lst[0]

    def generate_flashcard(self, concept, language):
        synsets = self.retrieve_synsets(concept, language)
        if not synsets:
            return None
        flashcard_info_lst = [self.extract_flashcard_info(s) for s in synsets]
        return concept, *self.select_flashcard_info(flashcard_info_lst)
