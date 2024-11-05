# backend/services/model_service.py
import tensorflow as tf
import numpy as np

class ModelService:
    def __init__(self, edible_model_path: str, species_model_path: str):
        """
        Initialize both models - one for edibility and one for species identification.
        """
        self.edible_model = tf.keras.models.load_model(edible_model_path)
        self.species_model = tf.keras.models.load_model(species_model_path)
        
        # Load species labels (you'll need to create this mapping)
        self.species_labels = {
            0: "Agaricus_arvensis",
            1: "Agaricus_augustus",
            2: "Agaricus_bisporus",
            3: "Agaricus_bitorquis",
            4: "Agaricus_bohusii",
            5: "Agaricus_campestris",
            6: "Agaricus_crocodilinus",
            7: "Agaricus_langei",
            8: "Agaricus_silvaticus",
            9: "Agaricus_subrufescens",
            10: "Agaricus_sylvaticus",
            11: "Agaricus_sylvicola",
            12: "Agrocybe_praecox",
            13: "Aleuria_aurantia",
            14: "Amanita_caesarea",
            15: "Amanita_ceciliae",
            16: "Amanita_crocea",
            17: "Amanita_excelsa",
            18: "Amanita_fulva",
            19: "Amanita_rubescens",
            20: "Amanita_sect._Vaginatae",
            21: "Apioperdon_pyriforme",
            22: "Armillaria_mellea",
            23: "Aspropaxillus_giganteus",
            24: "Auricularia_auricula-judae",
            25: "Auricularia_cornea",
            26: "Boletus_aereus",
            27: "Boletus_badius",
            28: "Boletus_edulis",
            29: "Boletus_pinophilus",
            30: "Boletus_reticulatus",
            31: "Butyriboletus_appendiculatus",
            32: "Calbovista_subsculpta",
            33: "Calocybe_gambosa",
            34: "Calvatia_gigantea",
            35: "Calvatia_utriformis",
            36: "Cantharellus_amethysteus",
            37: "Cantharellus_cibarius",
            38: "Cantharellus_cinnabarinus",
            39: "Cantharellus_friesii",
            40: "Cantharellus_pallens",
            41: "Cerioporus_squamosus",
            42: "Chalciporus_piperatus",
            43: "Chlorophyllum_rhacodes",
            44: "Chroogomphus",
            45: "Clavariaceae",
            46: "Clavulinaceae",
            47: "Clitocybe_nuda",
            48: "Clitocybe_odora",
            49: "Clitopilus_prunulus",
            50: "Coprinellus_micaceus",
            51: "Coprinus_comatus",
            52: "Cordyceps_militaris",
            53: "Cortinarius_caperatus",
            54: "Cortinarius_variicolor",
            55: "Craterellus_Lutescens",
            56: "Craterellus_cornucopioides",
            57: "Craterellus_tubaeformis",
            58: "Cuphophyllus_flavipes",
            59: "Cuphophyllus_pratensis",
            60: "Cuphophyllus_virgineus",
            61: "Cyclocybe_aegerita",
            62: "Cyclocybe_cylindracea",
            63: "Cyttaria_espinosae",
            64: "Fistulina_hepatica",
            65: "Flammulina_velutipes",
            66: "Fomitopsis_betulina",
            67: "Ganoderma_lucidum",
            68: "Gliophorus_laetus",
            69: "Grifola_frondosa",
            70: "Gyroporus_castaneus",
            71: "Hericium_cirrhatum",
            72: "Hericium_coralloides",
            73: "Hericium_erinaceus",
            74: "Hortiboletus_bubalinus",
            75: "Hortiboletus_rubellus",
            76: "Hydnum_repandum",
            77: "Hydnum_rufescens",
            78: "Hygrocybe_chlorophana",
            79: "Hygrocybe_coccinea",
            80: "Hygrocybe_miniata",
            81: "Hygrocybe_punicea",
            82: "Hygrocybe_splendidissima",
            83: "Hygrophorus_chrysodon",
            84: "Hymenopellis_radicata",
            85: "Hypomyces_lactifluorum",
            86: "Hypsizygus_tessellatus",
            87: "Hypsizygus_ulmarius",
            88: "Imleria_badia",
            89: "Infundibulicybe_geotropa",
            90: "Infundibulicybe_gibba",
            91: "Kalaharituber_pfeilii",
            92: "Kuehneromyces_mutabilis",
            93: "Laccaria_amethystina",
            94: "Laccaria_laccata",
            95: "Lactarius_camphoratus",
            96: "Lactarius_deliciosus",
            97: "Lactarius_deterrimus",
            98: "Lactarius_indigo",
            99: "Lactarius_salmonicolor",
            100: "Lactarius_subdulcis",
            101: "Lactarius_volemus",
            102: "Laetiporus_sulphureus",
            103: "Leccinum_albostipitatum",
            104: "Leccinum_aurantiacum",
            105: "Leccinum_duriusculum",
            106: "Leccinum_scabrum",
            107: "Leccinum_versipelle",
            108: "Lentinula_edodes",
            109: "Lepista_nuda",
            110: "Lepista_personata",
            111: "Leucoagaricus_leucothites",
            112: "Lycoperdon_excipuliforme",
            113: "Lycoperdon_perlatum",
            114: "Lycoperdon_pratense",
            115: "Lycoperdon_utriforme",
            116: "Lyophyllum_decastes",
            117: "Lyophyllum_shimeji",
            118: "Macrolepiota_mastoidea",
            119: "Macrolepiota_procera",
            120: "Marasmius_oreades",
            121: "Meripilus_giganteus",
            122: "Morchella_esculenta",
            123: "Morchella_importuna",
            124: "Morchella_semilibera",
            125: "Morchella_vulgaris",
            126: "Mucidula_mucida",
            127: "Mycena_galericulata",
            128: "Neoboletus_praestigiator",
            129: "Paralepista_flaccida",
            130: "Phallus_impudicus",
            131: "Phallus_indusiatus",
            132: "Pholiota_nameko",
            133: "Pleurotus",
            134: "Pleurotus_eryngii",
            135: "Pleurotus_ostreatus",
            136: "Pleurotus_pulmonarius",
            137: "Pluteus_cervinus",
            138: "Pluteus_umbrosus",
            139: "Polyporus_mylittae",
            140: "Polyporus_squamosus",
            141: "Polyporus_tuberaster",
            142: "Porpolomopsis_calyptriformis",
            143: "Pseudoclitocybe_cyathiformis",
            144: "Pseudohydnum_gelatinosum",
            145: "Rhizopogon_luteolus",
            146: "Rhodocollybia_butyracea",
            147: "Russula_claroflava",
            148: "Russula_cyanoxantha",
            149: "Russula_nigricans",
            150: "Russula_ochroleuca",
            151: "Russula_parazurea",
            152: "Russula_rosea",
            153: "Russula_undulata",
            154: "Russula_virescens",
            155: "Sarcoscypha_austriaca",
            156: "Sparassis_crispa",
            157: "Strobilomyces_strobilaceus",
            158: "Stropharia_rugosoannulata",
            159: "Suillellus_luridus",
            160: "Suillus_bovinus",
            161: "Suillus_granulatus",
            162: "Suillus_grevillei",
            163: "Suillus_luteus",
            164: "Suillus_tomentosus",
            165: "Suillus_variegatus",
            166: "Tremella_fuciformis",
            167: "Tricholoma_cingulatum",
            168: "Tricholoma_equestre",
            169: "Tricholoma_matsutake",
            170: "Tricholoma_terreum",
            171: "Tuber_aestivum",
            172: "Tuber_borchii",
            173: "Tuber_brumale",
            174: "Tuber_indicum",
            175: "Tuber_macrosporum",
            176: "Tuber_mesentericum",
            177: "Verpa_conica",
            178: "Volvariella_bombycina",
            179: "Volvariella_volvacea",
            180: "Volvopluteus_gloiocephalus",
            181: "Xerocomellus_chrysenteron",
            182: "Xerocomellus_porosporus",
            183: "Xerocomellus_pruinatus",
            184: "Xerocomus_subtomentosus",
        }

    def predict(self, image_array: np.ndarray) -> dict:
        """
        Make predictions using both models if appropriate.
        Returns dictionary with edibility prediction and species predictions if edible.
        """
        # First, check if it's edible
        edible_pred = self.edible_model.predict(image_array)[0][0]
        is_edible = edible_pred >= 0.5
        edible_confidence = float(edible_pred if is_edible else 1 - edible_pred)
        
        result = {
            "is_edible": bool(is_edible),
            "edible_confidence": edible_confidence
        }
        
        # If it's edible, predict species
        if is_edible:
            species_predictions = self.species_model.predict(image_array)[0]
            # Get indices of top 3 predictions
            top_3_indices = np.argsort(species_predictions)[-3:][::-1]
            
            # Calculate total confidence of top 3 predictions
            top_3_probabilities = species_predictions[top_3_indices]
            total_confidence = np.sum(top_3_probabilities)
            
            # Create list of top 3 species predictions
            species_predictions = [
                {
                    "species": self.species_labels[int(idx)],
                    "confidence": float(species_predictions[idx])
                }
                for idx in top_3_indices
            ]
            
            result.update({
                "species_predictions": species_predictions,
                "species_total_confidence": float(total_confidence)
            })
        
        return result