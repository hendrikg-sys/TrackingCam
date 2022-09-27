from tidecv import TIDE, datasets

tide = TIDE()
tide.evaluate(datasets.COCO(), datasets.COCOResult(
   path=r"F:\OneDrive\Desktop\code\Playground\result.json"), mode=TIDE.BOX)  # Use TIDE.MASK for masks
tide.summarize()  # Summarize the results as tables in the console
# Show a summary figure. Specify a folder and it'll output a png to that folder.
tide.plot()
