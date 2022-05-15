import aadharCard

aadhar = aadharCard.AadharData()

# Provide front page Image and Back Page Image in Below InfoExtractor function
# Due to identity, we have not provide actal image. Please check with your own aadhar card image for test
print(aadhar.InfoExtracter('./ConvertedImages/sample-1-front.jpg','./ConvertedImages/sample-1-back.jpg'))