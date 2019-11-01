for (int r = 0; r < mm.rows; r++)
{
    for (int c = 0; c < mm.cols; c++)
    {
        //得到指向每一个元素的指针
        Vec3f *ptr = (Vec3f*)(mm.data + r*mm.step[0] + c*mm.step[1]);
        count << *ptr << ",";  //打印元素

    }
    cout << endl;
}