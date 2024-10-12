1. Create images directory via running
```
mkdir images
```

2. Download images from [here](https://www.kaggle.com/datasets/derekkunowilliams/mushrooms) and put it in the images directory.

3. Run the `data_analysis.ipynb` notebook.

4. Run the `resizing.ipynb` notebook to resize the images to 256x256.


TO NOTE:
- We discovered duplicates in the original dataset, and have since manually removed them.
    - Armillaria_mellea is poisnous when not cooked, so we have removed it from the edible category.
    - Suillus_granulatus is edible, but was incorrectly labeled as poisonous too in the original dataset.
    - The following species were removed from the poisonous category as they overlapped with the deadly category:
        - Amanita_smithiana
        - Clitocybe_dealbata
        - Coprinopsis_atramentaria
        - Entoloma_sinuatum
        - Hypholoma_fasciculare
        - Lactarius_torminosus
        - Omphalotus_illudens
        - Omphalotus_japonicus
        - Pholiotina_rugosa
        - Russula_subnigricans
        - Tricholoma_equestre
        - Trogia_venenata