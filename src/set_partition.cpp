// v1 by ZXP4 on 26/03/13 0:11 UTC+8
// v2 on 26/03/13 21:53 UTC+8
// https://tieba.baidu.com/p/10530492439

#include <iostream>
#include <string>
#include <vector>

struct RunLength {
	RunLength() = default;
	RunLength(char ch_, int cnt_)
	    : ch(ch_)
	    , cnt(cnt_) {}
	char ch;
	int cnt;
};

int main() {
	std::cout << "input: ";

	std::string s;
	std::cin >> s;

	std::vector<int> hist(26);
	for (auto ch : s) {
		++hist[ch - 'a'];
	}

	const int n = s.size();

	int num_ch_available = n;
	std::vector<std::vector<RunLength>> plan(n);

	for (int subset_cnt = 1; subset_cnt <= n; subset_cnt++) {  // 尝试划分成 subset_cnt 个子集
		auto dfs = [&](auto &&self, int subset_id) -> bool {
			if ((subset_cnt - subset_id) > num_ch_available) {
				return false;
			}

			if (subset_id == subset_cnt) {
				for (int i = 0; i < 26; i++) {
					if (hist[i] != 0) {
						return false;
					}
				}
				return true;
			}

			// 枚举当前子集的其中一种选法，别忘了做到不重不漏
			for (int start_ch = 0; start_ch < 26; start_ch++) {
				for (int cnt = 1; cnt <= hist[start_ch]; cnt++) {
					// 确定了第一个字母以及出现次数
					// 先把第一个字母用掉
					hist[start_ch] -= cnt;
					num_ch_available -= cnt;
					plan[subset_id] = std::vector<RunLength>{ RunLength{ static_cast<char>('a' + start_ch), cnt } };

					// 从这里开始才是构造当前子集！
					int ok_ch_mask = 0;
					int num_ok_ch = 0;
					for (int ch = start_ch + 1; ch < 26; ch++) {
						if (hist[ch] >= cnt) {
							ok_ch_mask |= 1 << ch;
							++num_ok_ch;
						}
					}

					// 想办法枚举 ok_ch_mask 的每个子集
					// 方法：扩展的二进制枚举
					// 我在 https://tieba.baidu.com/p/9645529993 记录过
					int ok_ch_mask_subset = ok_ch_mask;
					for (int i = 0; i < (1 << num_ok_ch); i++) {
						plan[subset_id].resize(1);

						// 使用字母
						for (int j = start_ch + 1; j < 26; j++) {
							if ((ok_ch_mask_subset >> j & 1) == 1) {
								hist[j] -= cnt;
								num_ch_available -= cnt;
								plan[subset_id].emplace_back(static_cast<char>('a' + j), cnt);
							}
						}

						// 递归构造下一个子集
						if (self(self, subset_id + 1)) {
							return true;
						}

						// 恢复现场：其他字母
						for (int j = start_ch + 1; j < 26; j++) {
							if ((ok_ch_mask_subset >> j & 1) == 1) {
								hist[j] += cnt;
								num_ch_available += cnt;
							}
						}

						ok_ch_mask_subset = (ok_ch_mask_subset - 1) & ok_ch_mask;
					}

					// 恢复现场：第一个字母
					hist[start_ch] += cnt;
					num_ch_available += cnt;
				}
			}

			return false;
		};

		if (dfs(dfs, 0)) {
			std::cout << "minimum subset cnt: " << subset_cnt << '\n';

			std::cout << "solution:\n";
			for (int i = 0; i < subset_cnt; i++) {
				std::cout << '[' << i << "] ";
				for (auto rl : plan[i]) {
					std::cout << std::string(rl.cnt, rl.ch);
				}
				std::cout << '\n';
			}

			return 0;
		}
	}

	return 0;
}
