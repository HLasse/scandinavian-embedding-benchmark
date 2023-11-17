The following tables contains description of all the dataset in the benchmark along with with their main score, what type of task it as, what languages it covers and some statistics for each dataset. The domains follows the categories used in the [Universal Dependencies project](https://universaldependencies.org).

<!--START_TABLE-->
| Dataset                                                                                                                                                  | Description                                                                                                                                                                                                | Main Score   | Languages              | Type           | Domains                                                  |   Number of Documents | Mean Length of Documents (characters)   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-----------------------|:---------------|:---------------------------------------------------------|----------------------:|:----------------------------------------|
| [Angry Tweets](https://aclanthology.org/2021.nodalida-main.53/)                                                                                          | A sentiment dataset with 3 classes (positiv, negativ, neutral) for Danish tweets                                                                                                                           | Accuracy     | da                     | Classification | social                                                   |                  1047 | 156.15 (std: 82.02)                     |
| [Bornholm Parallel](https://aclanthology.org/W19-6138/)                                                                                                  | Danish Bornholmsk Parallel Corpus. Bornholmsk is a Danish dialect spoken on the island of Bornholm, Denmark. Historically it is a part of east Danish which was also spoken in Scania and Halland, Sweden. | F1           | da, da-bornholm        | BitextMining   | poetry, wiki, fiction, web, social                       |                  1000 | 44.36 (std: 41.22)                      |
| [DKHate](https://aclanthology.org/2020.lrec-1.430/)                                                                                                      | Danish Tweets annotated for Hate Speech either being Offensive or not                                                                                                                                      | Accuracy     | da                     | Classification | social                                                   |                   329 | 88.18 (std: 168.30)                     |
| [Da Political Comments](https://huggingface.co/datasets/danish_political_comments)                                                                       | A dataset of Danish political comments rated for sentiment                                                                                                                                                 | Accuracy     | da                     | Classification | social                                                   |                  7206 | 69.60 (std: 62.85)                      |
| [DaLAJ](https://spraakbanken.gu.se/en/resources/superlim)                                                                                                | A Swedish dataset for linguistic acceptability. Available as a part of Superlim.                                                                                                                           | Accuracy     | sv                     | Classification | fiction, non-fiction                                     |                   888 | 120.77 (std: 67.95)                     |
| [LCC](https://github.com/fnielsen/lcc-sentiment)                                                                                                         | The leipzig corpora collection, annotated for sentiment                                                                                                                                                    | Accuracy     | da                     | Classification | legal, web, news, social, fiction, non-fiction, academic |                   150 | 118.73 (std: 57.82)                     |
| [Language Identification](https://aclanthology.org/2021.vardial-1.8/)                                                                                    | A dataset for Nordic language identification.                                                                                                                                                              | Accuracy     | da, sv, nb, nn, is, fo | Classification | wiki                                                     |                  3000 | 78.23 (std: 48.54)                      |
| [Massive Intent](https://arxiv.org/abs/2204.08582#:~:text=MASSIVE%20contains%201M%20realistic%2C%20parallel,diverse%20languages%20from%2029%20genera.)   | MASSIVE: A 1M-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-Diverse Languages                                                                                          | Accuracy     | da, nb, sv             | Classification | spoken                                                   |                 15021 | 34.65 (std: 16.99)                      |
| [Massive Scenario](https://arxiv.org/abs/2204.08582#:~:text=MASSIVE%20contains%201M%20realistic%2C%20parallel,diverse%20languages%20from%2029%20genera.) | MASSIVE: A 1M-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-Diverse Languages                                                                                          | Accuracy     | da, nb, sv             | Classification | spoken                                                   |                 15021 | 34.65 (std: 16.99)                      |
| [NoReC](https://aclanthology.org/L18-1661/)                                                                                                              | A Norwegian dataset for sentiment classification on reviews                                                                                                                                                | Accuracy     | nb                     | Classification | reviews                                                  |                  2048 | 89.62 (std: 61.21)                      |
| [Norwegian parliament](https://huggingface.co/datasets/NbAiLab/norwegian_parliament)                                                                     | Norwegian parliament speeches annotated for sentiment                                                                                                                                                      | Accuracy     | nb                     | Classification | spoken                                                   |                  2400 | 1897.51 (std: 1988.62)                  |
| [ScaLA](https://aclanthology.org/2023.nodalida-1.20/)                                                                                                    | A linguistic acceptability task for Danish, Norwegian Bokmål Norwegian Nynorsk and Swedish.                                                                                                                | Accuracy     | da, nb, sv, nn         | Classification | fiction, news, non-fiction, spoken, blog                 |                 74846 | 102.50 (std: 56.10)                     |
| [SweFAQ](https://spraakbanken.gu.se/en/resources/superlim)                                                                                               | A Swedish QA dataset derived from FAQ                                                                                                                                                                      | Ndcg_at_10   | sv                     | Retrieval      | non-fiction, web                                         |                  1539 | 236.21 (std: 225.72)                    |
| [SweReC](https://aclanthology.org/2023.nodalida-1.20/)                                                                                                   | A Swedish dataset for sentiment classification on review                                                                                                                                                   | Accuracy     | sv                     | Classification | reviews                                                  |                  2048 | 318.83 (std: 499.57)                    |
<!--END_TABLE-->