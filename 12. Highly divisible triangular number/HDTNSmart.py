__author__ = 'Ray'

import HDTNBruteFocus

class HDTNSmart(HDTNBruteFocus.HDTNBruteFocus):

    @staticmethod
    def search(upperBound):
        """
        based on the observation that n and n+1 have no common factor except 1.
        similar to {n, (n+1)/2} or {n/2, n+1}
        so we can time the count of both part to get the total count
        :param upperBound:
        :return:
        """
        factorCountList = [0, 1]
        i = 1
        count = 1
        while(1):
            factorCountList.append(HDTNSmart.factororCount(i+1))
            if i % 2 == 0:
                count = factorCountList[int(i/2)] * factorCountList[i+1]
            else:
                count = factorCountList[int((i+1)/2)] * factorCountList[i]
            if count > upperBound:
                return (i, HDTNSmart.computeTriangularNumber(i))
            i += 1