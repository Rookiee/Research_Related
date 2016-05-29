#ifndef READ_DATA_FROM_FILE_H
#define READ_DATA_FROM_FILE_H
/* 说明：
	从文本文件中读取两列或三列的数据，可分别保存到：
		1. std::list<std::vector<float> >;  
		2. std::vector<float> 
		3. 一维数组 */
#include <fstream>
#include <string>

#include <vector>
#include <list>
/*******************************************************************************************************/
/* 函数1： 从文件读取 numeric data （两列数据或三行数据）*/
/* 返回 std::list< std::vector<float> > */
/* 结构：整个文件是一个list， 每一行是一个vector */
std::list< std::vector<float> >  getDataFromTxttoList(std::string fileName, int cols = 3)
{

	float a, b, c = 0;
	std::list < std::vector<float> > myData;

	std::ifstream inFile;
	inFile.open(fileName.c_str());

	if (inFile.is_open())
	{
		if (cols == 3)
		{
			while (inFile >> a >> b >> c)
			{
				std::vector<float> tempVec;
				tempVec.push_back(a);
				tempVec.push_back(b);
				tempVec.push_back(c);
				myData.push_back(tempVec);
			}
		}

		if (cols == 2)
		{
			while (inFile >> a >> b)
			{
				std::vector<float> tempVec;
				tempVec.push_back(a);
				tempVec.push_back(b);
				myData.push_back(tempVec);
			}
		}

		/* 如果读取更多列数据，以此在下添加*/
		/*if (cols == 4)
		{

		}*/
	}
	inFile.close();
	return myData;
}

/* 函数4： 保存list到txt文件 */
void saveDataFromListtoTxt(std::string fileName, std::list< std::vector<float> > &myList){
	std::ofstream outFile;
	outFile.open(fileName.c_str(), std::ios_base::out );
	if (outFile.is_open()){
		for (std::list<std::vector<float> >::iterator itList = myList.begin(); itList != myList.end(); ++itList){
			for (std::vector<float>::iterator itVec = (*itList).begin(); itVec != (*itList).end(); ++itVec){
				outFile << *itVec << " ";
			}
			outFile << std::endl;
		}
	}
	outFile.close();
}
/*******************************************************************************************************/

/* 函数2： 调用函数1，将得到的list转换为1个vector */
std::vector<float> getDataFromTxtto1Vector(std::string fileName, int cols = 3){
	std::list< std::vector<float> > myData = getDataFromTxttoList(fileName, cols);
	std::vector<float> myVec;
	for (std::list <std::vector<float> >::iterator itList = myData.begin(); itList != myData.end(); ++itList){
		for (std::vector<float>::iterator itVec = (*itList).begin(); itVec != (*itList).end(); ++itVec){
			myVec.push_back(*itVec);
		}
	}

	return myVec;
}
/* 函数5： 保存vector到txt文件 */
void saveDataFrom1VectortoTxt(std::string fileName, std::vector<float>& myVec, int cols = 3){
	std::ofstream outFile;
	outFile.open(fileName.c_str(), std::ios_base::out );
	if (outFile.is_open()){
		if (cols == 1){
			for (std::vector<float> ::iterator itVec = myVec.begin(); itVec != myVec.end(); ++itVec){
				outFile << *itVec << std::endl;
			}
			
		}
		if (cols == 2){
			for (std::vector<float> ::iterator itVec = myVec.begin(); itVec != myVec.end(); itVec += 2){
				outFile << *itVec << " " << *(itVec + 1) << std::endl;
			}
		}

		if (cols == 3){
			for (std::vector<float> ::iterator itVec = myVec.begin(); itVec != myVec.end(); itVec += 3){
				outFile << *itVec << " " << *(itVec + 1) << " " << *(itVec + 2) << std::endl;
			}
		}
	}

	outFile.close();
}
/*******************************************************************************************************/
/* 函数3： 将Vector转换为1维数组
 * Example:
 * Before call below function, call getDataFromTxt1Vector() firstly: 
 *      std::vector<float> myVec = getDataFromTxtto1Vector(filename, cols);
 * then, get the length of the vector:
 *      int numOfElement = myVec.size();
 * next, create an array:
 *      float* myArr = new float[numOfElement];
 * now, using the below function:
 *      getDataFromTxtto1Array(myVec, myArr);
 * with this step, we can use the array directly;
 *      process(myArr);
 * finally, delete the memory
 * 		delete []myArr;
 */
void  getDataFromTxtto1Array(std::vector<float>& tempVec, float* tempArr)
{
    for(std::vector<float>::iterator itVec = tempVec.begin(); itVec != tempVec.end(); ++itVec){
        *tempArr = *itVec;
        if(itVec != tempVec.end()-1){
            tempArr++;
        }
    }
}
void saveDataFrom1ArraytoTxt(std::string fileName, float* myArr, size_t num, int cols = 3){
	std::ofstream outFile;
	outFile.open(fileName.c_str(), std::ios_base::out);
	if (outFile.is_open()){
		if (cols == 3){
			for (size_t i = 0; i < num; i += 3){
				outFile << myArr[i] << " " << myArr[i + 1] << " " << myArr[i + 2] << std::endl;
			}
		}
		else if (cols == 2){
			for (size_t i = 0; i < num; i += 2){
				outFile << myArr[i] << " " << myArr[i + 1] << " " << std::endl;
			}
		}
		else
			for (size_t i = 0; i < num; ++i){
				outFile << myArr[i] << std::endl;
			}
	}

	outFile.close();
}

/*******************************************************************************************************/


/*
using namespace std;
int main(void)
{

	// 第三个函数测试代码
    std::vector<float> myVector = getDataFromTxtto1Vector("testdata.xlsx");
    int numOfVec = myVector.size();
    float* myArr = new float[numOfVec];
    getDataFromTxtto1Array(myVector, myArr);
    for(int i = 0; i< numOfVec; ++i){
        cout << myArr[i] << endl;
    }
    delete []myArr;




	//// 测试函数2 返回到单一vector的代码
	//std::vector<float> myVec = getDataFromTxtto1Vector("testdata.txt");
	//for (vector<float>::iterator it = myVec.begin(); it != myVec.end(); ++it){
	//	cout << *it << endl;
	//}


	// 测试函数1 读到链表的代码
	// list<vector<float> > myData = getDataFromTxttoList("testdata.txt");
	// for (list<vector<float> >::iterator itList = myData.begin(); itList != myData.end(); ++itList){
	// 	for (vector<float>::iterator itVec = (*itList).begin(); itVec != (*itList).end(); ++itVec){
	// 		cout << *itVec << "    ";
	// 	}
	// 	cout << endl;
	// }

	cout << "DONE" << endl;

    return 0;
}
*/

#endif
